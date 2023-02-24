"""This file contains the models for the database"""
from sqlalchemy import UniqueConstraint

from main import app, db


class Adventures(db.Model):
    """This class contains the model for the adventures table"""

    id = db.Column(db.Integer, primary_key=True)
    adventure_title = db.Column(db.String)
    adventure_hook = db.Column(db.String)
    adventure_plot = db.Column(db.String)
    adventure_climax = db.Column(db.String)
    adventure_resolution = db.Column(db.String)
    adventure_npcs = db.Column(db.String)
    entities = db.relationship(
        "Entities", back_populates="adventure", foreign_keys="Entities.adventure_id"
    )

    def __repr__(self) -> str:
        return f"<Adventures {self.adventure_title}>"

    @staticmethod
    def get_adventures(adventure_id=None) -> list:
        """Get all adventures from database

        Returns:
            list: list containing all adventures
        """
        if adventure_id:
            db_adventures = Adventures.query.filter_by(id=adventure_id)
        else:
            db_adventures = Adventures.query.all()
        adventures = []
        for adventure in db_adventures:
            adventures.append(
                {
                    "id": adventure.id,
                    "AdventureTitle": adventure.adventure_title,
                    "AdventureHook": adventure.adventure_hook,
                    "AdventurePlot": adventure.adventure_plot,
                    "AdventureClimax": adventure.adventure_climax,
                    "AdventureResolution": adventure.adventure_resolution,
                    "AdventureNPCs": adventure.adventure_npcs,
                }
            )
        return adventures

    @staticmethod
    def delete_adventures(adventure_ids: list) -> None:
        """Delete adventure(s) from database

        Args:
            adventure_id (int, optional): ID of adventure to delete. Defaults to None.
        """
        if adventure_ids:
            Adventures.query.filter(Adventures.id.in_(adventure_ids)).delete(
                synchronize_session="fetch"
            )
            db.session.commit()


class Entities(db.Model):
    """Model for Named Entities recognized in adventure text

    Args:
        Base (Base): Parent Class

    Returns:
        Entity: Object of Class Entity
    """

    id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(255))
    adventure_id = db.Column(db.Integer, db.ForeignKey("adventures.id"))
    adventure = db.relationship("Adventures", back_populates="entities")


class AdventureNPCs(db.Model):
    """This class contains the model for the adventure_npcs table"""

    __tablename__ = "adventure_npcs"
    id = db.Column(db.Integer, primary_key=True)
    adventure_id = db.Column(db.Integer, db.ForeignKey("adventures.id"))
    npc_name = db.Column(db.String)
    npc_background = db.Column(db.String)
    npc_stats = db.Column(db.String)
    npc_game_system = db.Column(db.String)

    __table_args__ = (
        UniqueConstraint("adventure_id", "npc_name"),
    )  # In order to implement this with an already existing db, need to manually delete table and recreate it

    @staticmethod
    def get_NPCs(adventure_id):
        npcs = AdventureNPCs.query.filter_by(adventure_id=adventure_id).all()
        return [npc.npc_name for npc in npcs]

    def __repr__(self):
        return f"<AdventureNPCs {self.npc_name}>"


class AdventureLocations(db.Model):
    """This class contains the model for the adventure_npcs table"""

    __tablename__ = "adventure_locations"

    id = db.Column(db.Integer, primary_key=True)
    adventure_id = db.Column(db.Integer, db.ForeignKey("adventures.id"))
    location_name = db.Column(db.String)

    @staticmethod
    def get_locations(adventure_id) -> list:
        """Get all locations from adventure

        Returns:
            list: list containing all locations
        """
        locations = AdventureLocations.query.filter_by(adventure_id=adventure_id).all()

        locations_list = []
        for location in locations:
            locations_list.append(location.location_name)

        return locations_list

    def __repr__(self):
        return f"<AdventureLocation {self.location_name}>"


with app.app_context():
    db.create_all()
