'''This file contains the models for the database'''
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///fantasy_fabricator.db')

Base = declarative_base()


class Adventures(Base):
    '''This class contains the model for the adventures table'''
    __tablename__ = 'adventures'

    id = Column(Integer, primary_key=True)
    adventure_title = Column(String)
    adventure_hook = Column(String)
    adventure_plot = Column(String)
    adventure_climax = Column(String)
    adventure_resolution = Column(String)
    adventure_npcs = Column(String)

    def __init__(self, adventure_title, adventure_hook, adventure_plot,
                 adventure_climax, adventure_resolution, adventure_npcs):
        self.adventure_title = adventure_title
        self.adventure_hook = adventure_hook
        self.adventure_plot = adventure_plot
        self.adventure_climax = adventure_climax
        self.adventure_resolution = adventure_resolution
        self.adventure_npcs = adventure_npcs

    def __repr__(self):
        return f'<Adventure {self.adventure_title}>'


class AdventureNPCs(Base):
    '''This class contains the model for the adventure_npcs table'''
    __tablename__ = 'adventure_npcs'

    id = Column(Integer, primary_key=True)
    adventure_id = Column(Integer, ForeignKey('adventures.id'))
    npc_name = Column(String)

    def __init__(self, adventure_id, npc_name):
        self.adventure_id = adventure_id
        self.npc_name = npc_name

    def __repr__(self):
        return f'<Adventure_NPC {self.npc_name}>'


Base.metadata.create_all(engine)
