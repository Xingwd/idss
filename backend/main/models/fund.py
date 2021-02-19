from main import db


class Overview(db.Model):
    __bind_key__ = 'seer_fund'
    __tablename__ = 'overview'
    code = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Fund {}[{}]>'.format(self.name, self.code)
