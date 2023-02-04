'''This file contains the models for the database'''
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///fantasy_fabricator.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Adventures(Base):
    """This class contains the model for the adventures table"""
    __tablename__ = 'adventures'

    id = Column(Integer, primary_key=True)
    adventure_title = Column(String)
    adventure_hook = Column(String)
    adventure_plot = Column(String)
    adventure_climax = Column(String)
    adventure_resolution = Column(String)
    adventure_npcs = Column(String)
    entities = relationship("Entities",
                            back_populates="adventure",
                            foreign_keys="Entities.adventure_id")

    def __init__(self, adventure_title, adventure_hook, adventure_plot,
                 adventure_climax, adventure_resolution, adventure_npcs):
        self.adventure_title = adventure_title
        self.adventure_hook = adventure_hook
        self.adventure_plot = adventure_plot
        self.adventure_climax = adventure_climax
        self.adventure_resolution = adventure_resolution
        self.adventure_npcs = adventure_npcs

    def __repr__(self) -> str:
        return f'<Adventures {self.adventure_title}>'

    @staticmethod
    def get_adventures(adventure_id=None) -> list:
        """Get all adventures from database

        Returns:
            list: list containing all adventures
        """
        session = Session()
        if adventure_id:
            db_adventures = session.query(Adventures).filter_by(id=adventure_id)
        else:
            db_adventures = session.query(Adventures).all()
        adventures = []
        for adventure in db_adventures:
            adventures.append({
                'id': adventure.id,
                'AdventureTitle': adventure.adventure_title,
                'AdventureHook': adventure.adventure_hook,
                'AdventurePlot': adventure.adventure_plot,
                'AdventureClimax': adventure.adventure_climax,
                'AdventureResolution': adventure.adventure_resolution,
                'AdventureNPCs': adventure.adventure_npcs
            })
        return adventures

    @staticmethod
    def delete_adventures(adventure_ids: list) -> None:
        """Delete adventure(s) from database

        Args:
            adventure_id (int, optional): ID of adventure to delete. Defaults to None.
        """
        session = Session()
        if adventure_ids:
            adventures = session.query(Adventures).filter(Adventures.id.in_(adventure_ids))
            print(adventures)
            adventures.delete(synchronize_session=False)
            session.commit()

class Entities(Base):
    """Model for Named Entities recognized in adventure text

    Args:
        Base (Base): Parent Class

    Returns:
        Entity: Object of Class Entity
    """
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    entity_name = Column(String(255))
    adventure_id = Column(Integer, ForeignKey('adventures.id'))
    adventure = relationship("Adventures", back_populates="entities")

    def __init__(self, entity_name, adventure_id):
        self.entity_name = entity_name
        self.adventure_id = adventure_id


class AdventureNPCs(Base):
    '''This class contains the model for the adventure_npcs table'''
    __tablename__ = 'adventure_npcs'

    id = Column(Integer, primary_key=True)
    adventure_id = Column(Integer, ForeignKey('adventures.id'))
    npc_name = Column(String)

    @staticmethod
    def get_NPCS(adventure_id) -> list:
        """Get all NPCs from adventure

        Returns:
            list: list containing all adventures
        """
        session = Session()
        db_NPC = session.query(AdventureNPCs).filter_by(adventure_id=adventure_id)

        npc_list = []
        for NPC in db_NPC:
            npc_list.append(NPC.npc_name)

        return npc_list
    def __init__(self, adventure_id, npc_name):
        self.adventure_id = adventure_id
        self.npc_name = npc_name

    def __repr__(self):
        return f'<Adventure_NPCs {self.npc_name}>'


class AdventureLocations(Base):
    '''This class contains the model for the adventure_npcs table'''
    __tablename__ = 'adventure_locations'

    id = Column(Integer, primary_key=True)
    adventure_id = Column(Integer, ForeignKey('adventures.id'))
    location_name = Column(String)

    def __init__(self, adventure_id, location_name):
        self.adventure_id = adventure_id
        self.location_name = location_name

    def __repr__(self):
        return f'<Adventure_NPCs {self.location_name}>'

Base.metadata.create_all(engine)
