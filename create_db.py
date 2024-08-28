     
from app import app,db,Student
 
with app.app_context():
    db.create_all()
 
    joshua = Student('Joshua',2,'male')
    albert = Student('Albert',12,'male')
    herbert = Student('Herbert',32,'male')
    caleb = Student('Caleb',78,'male')
    jalilu = Student('Jalilu',39,'male')
    pokuaa = Student('Pokuaa',15,'female')
    nicole = Student('Nicole',45,'female')
 
    db.session.add_all([joshua,albert,
                        herbert,caleb,
                        jalilu,pokuaa,
                        nicole])
    db.session.commit()