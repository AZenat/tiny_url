from sqlalchemy.orm import Session
from .url import URL

def create_db_url(session: Session, url: URL):
    session.add(url)
    session.commit()
    session.refresh(url)


def get_db_url(session: Session, short_url: str) -> URL:
    return session.query(URL).filter(URL.short_url == short_url).first()


def increment_db_click(session: Session, url: URL):
    url.clicks += 1
    session.add(url)
    session.commit()
