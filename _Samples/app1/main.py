from flask import Flask
from _Samples.app1.data import db_session
from _Samples.app1.data.__all_models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    amount = 6
    ##### ADD PERSONAL
    surnames = ["Scott", "Jackson", "Kamado", "Carry", "Brown", "Freeman"]
    names = ["Riddley", "Michael", "Manfred", "Ben", "John", "Albert"]
    ages = [21, 23, 34, 29, 38, 25]
    positions = ["captain", "private", "corporal", "private first class", "staff-sergeant", "private"]
    specialities = ["research engineer", "research engineer", "life support engineer",
                    "drone pilot", "medic", "builder"]
    addresses = ["module 1", "module 1", "module 2", "module 3", "module 2", "module 3"]
    emails = ["scott_chief@mars.org", "michael_singer@mars.org", "foreigner_guy@mars.org",
              "arma_III@mars.org", "stereotypical_name@mars.org", "science4life@mars.org"]
    db_sess = db_session.create_session()
    for i in range(amount):
        user = User()
        user.surname = surnames[i]
        user.name = names[i]
        user.age = ages[i]
        user.position = positions[i]
        user.speciality = specialities[i]
        user.address = addresses[i]
        user.email = emails[i]
        db_sess.add(user)
    ##### ADD JOB
    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "1, 3"
    #job.data is default (now)
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    main()