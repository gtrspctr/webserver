from . import db
from datetime import datetime

# Define database model
class RemoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    isp = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    country = db.Column(db.Text, nullable=False)
    method = db.Column(db.String(7), nullable=False)
    agent = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"RemoteRequest('{self.ip}')"
    
    def serialize(self):
        return {
            "id": self.id,
            "ip": self.ip,
            "isp": self.isp,
            "city": self.city,
            "country": self.country,
            "method": self.method,
            "agent": self.agent,
            "created_at": str(self.created_at)
        }