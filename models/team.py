from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bracket_id = db.Column(db.Integer, db.ForeignKey('bracket.id'), nullable=False)

    def __repr__(self):
        return f'<Team {self.name}>'
