from sqlalchemy.schema import ForeignKey
from programmerJobs import db
# from programmerJobs import app
# import programmerJobs

job_languages = db.Table('job_require_language',
                         db.Column('job_id', db.Integer, db.ForeignKey('job.job_id')),
                         db.Column('language_id', db.Integer, db.ForeignKey('language.language_id')))
job_skillsets = db.Table('job_require_skillset',
                         db.Column('job_id', db.Integer, db.ForeignKey('job.job_id')),
                         db.Column('skillset_id', db.Integer, db.ForeignKey('skillset.skillset_id')))


class Job(db.Model):
    """
    This is the Job model and has the following attributes:
    job_id (Integer) - A unique indentifier
    job_title (Text) - Job title
    job_description (Text) - Job description
    link (Text) - URL of the job posting on the company's website
    locationid (Integer) - Identifier for the location of the job
    companyid (Integer) - Identifer for the company
    skillsets (Iterable) - Iterable of skillsets needed for job
    languages (Iterable) - Iterable of languages needed for job
    """
    __tablename__ = 'job'

    job_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.Text)
    job_description = db.Column(db.Text)
    link = db.Column(db.Text)
    location_id = db.Column(db.Integer, ForeignKey('location.location_id'))
    company_id = db.Column(db.Integer, ForeignKey('company.company_id'))

    languages = db.relationship('Language', secondary=job_languages, backref='job', lazy='dynamic')
    skillsets = db.relationship('Skillset', secondary=job_skillsets, backref='job', lazy='dynamic')

    def __init__(self, job_id, title, location_id, company_id, description, link):
        self.job_id = job_id
        self.job_title = title
        self.location_id = location_id
        self.company_id = company_id
        self.job_description = description
        self.link = link

    def serialize(self):
        return {
            'job_id': self.job_id,
            'job_title': self.job_title,
            'location_id': self.location_id,
            'company_id': self.company_id,
            'job_description': self.job_description,
            'link': self.link
            }

    def __repr__(self):
        return '<Job %r>' % self.job_title


class Company(db.Model):
    """
    This is the Company model and has the following attributes:
    company_id (Integer) - Unique identifier
    company_name (Text) - Name of the company
    company_description (Text) - Description of the company
    company_image (Text) - URL for company image
    company_site (Text) - URL for company
    """
    __tablename__ = 'company'

    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.Text)
    company_description = db.Column(db.Text)
    company_image = db.Column(db.Text)
    company_site = db.Column(db.Text)
    twitter_id = db.Column(db.Text)

    def __init__(self, company_id, name, description, image, site, twitter_id):
        self.company_id = company_id
        self.company_name = name
        self.company_description = description
        self.company_image = image
        self.company_site = site
        self.twitter_id = twitter_id

    def serialize(self):
        # twitter_id = '591372267679944704'
        # # Google
        # if self.company_id == 1:
        #     twitter_id = '591372267679944704'
        # # Oracle
        # elif self.company_id == 2:
        #     twitter_id = '591370969584828416'
        # # Amazon
        # elif self.company_id == 3:
        #     twitter_id = '591372631082831872'
        # # Facebook
        # elif self.company_id == 4:
        #     twitter_id = '591372791414267904'
        # # Twitter
        # elif self.company_id == 5:
        #     twitter_id = '591372946406408192'
        # # LinkedIn
        # elif self.company_id == 6:
        #     twitter_id = '591373056414650369'
        # # IBM
        # elif self.company_id == 7:
        #     twitter_id = '591373157191143424'
        # # Dropbox
        # elif self.company_id == 8:
        #     twitter_id = '591373287705354240'
        # # Rackspace
        # elif self.company_id == 9:
        #     twitter_id = '591373403317121024'
        # # Indeed
        # elif self.company_id == 10:
        #     twitter_id = '591370969584828416'
            
        return {
            'company_id': self.company_id,
            'company_name': self.company_name,
            'company_image': self.company_image,
            'company_description': self.company_description,
            'company_site': self.company_site,
            'twitter_id': self.twitter_id
            }

    def __repr__(self):
        return '<company %r>' % self.company_name


class Language(db.Model):
    """
    This is the Language model and has the following attributes:
    language_id (Integer) - Unique identifier
    language_name (Text) - Name of the programming language
    language_description (Text) - Description of the programming language
    language_wiki_description (Text) - URL for the smaller image of the programming language
    language_wiki_link (Text) - URL for the larger image of the programming language
    """
    __tablename__ = 'language'

    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.Text)
    language_image = db.Column(db.Text)
    language_wiki_description = db.Column(db.Text)
    language_description = db.Column(db.Text)
    language_wiki_link = db.Column(db.Text)

    def __init__(self, language_id, name, image, wiki_description, description, wiki_link):
        self.language_id = language_id
        self.language_name = name
        self.language_image = image
        self.language_wiki_description = wiki_description
        self.language_description = description
        self.language_wiki_link = wiki_link

    def serialize(self):
        return {
            'language_id': self.language_id,
            'language_name': self.language_name,
            'language_image': self.language_image,
            'language_wiki_description': self.language_wiki_description,
            'language_description': self.language_description,
            'language_wiki_link': self.language_wiki_link
            }

    def __repr__(self):
        return '<Language %r>' % self.language_name


class Location(db.Model):
    """
    This is the Location model and has the following attributes:
    location_id (Integer) - Unique Identifier
    location_name (Text) - Name of the location
    location_description (Text) - Description of the location
    location_image (Text) - URL for the location image
    """
    __tablename__ = 'location'

    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.Text)
    location_description = db.Column(db.Text)
    location_image = db.Column(db.Text)

    def __init__(self, location_id, name, description, image):
        self.location_id = location_id
        self.location_name = name
        self.location_description = description
        self.location_image = image

    def serialize(self):
        return {
            'location_id': self.location_id,
            'location_name': self.location_name,
            'location_description': self.location_description,
            'location_image': self.location_image
            }

    def __repr__(self):
        return '<Location %r>' % self.location_name


class Skillset(db.Model):
    """
    This is the Skillset model and has the following attributes:
    skillset_id (Integer)  - Unique identifier
    skillset_name (Text) - Name of the skillset
    skillset_description (Text) - Description of the skillset
    """
    __tablename__ = 'skillset'

    skillset_id = db.Column(db.Integer, primary_key=True)
    skillset_name = db.Column(db.Text)
    skillset_description = db.Column(db.Text)
    skillset_image = db.Column(db.Text)
    skillset_wiki_description = db.Column(db.Text)
    skillset_wiki_link = db.Column(db.Text)

    def __init__(self, skillset_id, name, description, image, wiki_description, wiki_link):
        self.skillset_id = skillset_id
        self.skillset_name = name
        self.skillset_description = description
        self.skillset_image = image
        self.skillset_wiki_description = wiki_description
        self.skillset_wiki_link = wiki_link

    def serialize(self):
        return {
            'skillset_id': self.skillset_id,
            'skillset_name': self.skillset_name,
            'skillset_description': self.skillset_description,
            'skillset_image': self.skillset_image,
            'skillset_wiki_description': self.skillset_wiki_description,
            'skillset_wiki_link': self.skillset_wiki_link
            }

    def __repr__(self):
        return '<Skillset %r>' % self.skillset_name


class Member(db.Model):
    """
    This is the Member model and has the following attributes:
    member_id (Integer) - Unique identifier
    member_name (Text) - Name of a member
    member_bio (Text) - Biography for a member
    member_major_responsibility (Text) - Major responsibity for a member
    member_commit (Integer) - Number of commit
    member_issue (Integer) - Number of issue
    member_unittest (Integer) - Number of unittest
    member_image (Text) - Image directory
    member_leader (Integer) - Number of leader
    """

    __tablename__ = 'member'

    member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.Text)
    member_bio = db.Column(db.Text)
    member_major_responsibility = db.Column(db.Text)
    member_commit = db.Column(db.Integer)
    member_issue = db.Column(db.Integer)
    member_unittest = db.Column(db.Integer)
    member_image = db.Column(db.Text)
    member_leader = db.Column(db.Integer)

    def __init__(self, member_id, name, bio, major_responsibility, commits, issues, unit_tests, image, leader):
        self.member_id = member_id
        self.member_name = name
        self.member_bio = bio
        self.member_major_responsibility = major_responsibility
        self.member_commit = commits
        self.member_issue = issues
        self.member_unittest = unit_tests
        self.member_image = image
        self.member_leader = leader

    def serialize(self):
        return {
            'member_id': self.member_id,
            'member_name': self.member_name,
            'member_bio': self.member_bio,
            'member_major_responsibility': self.member_major_responsibility,
            'member_commit': self.member_commit,
            'member_issue': self.member_issue,
            'member_unittest': self.member_unittest,
            'member_image': self.member_image,
            'member_leader': self.member_leader
            }

    def __repr__(self):
        return '<Member %r>' % self.member_name
