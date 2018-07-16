from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from pyramid.config import Configurator
from nbp_task.models import initialize_sql, exchange_rate


def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()
    request.add_finished_callback(cleanup)

    return session


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.scan('nbp_task.models')
    config.scan('.views')
    engine = engine_from_config(settings, url='sqlite:///currency_db.sqlite')
    config.add_request_method(db, reify=True)
    initialize_sql(engine)
    config.registry.dbmaker = sessionmaker(bind=engine)
    config.add_route('home', '/')
    config.add_route('results', '/results')
    return config.make_wsgi_app()
