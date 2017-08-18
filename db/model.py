# -*-coding:utf-8 -*-

from db.db_basic import Base
from db.table import *
from db.table import style

class Style(Base):
	__table__ = style

class Playlist(Base):
	__table__ = playlist


class Song(Base):
	__table__ = song


class Comment(Base):
	__table__ = comment

class User(Base):
	__table__ = user




