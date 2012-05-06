###
# Controller for main presentation
#
###
from util import AppRequestHandler
import csv
from StringIO import StringIO
from models.study import Study

class gwasReader(AppRequestHandler):
    def get(self):
        self.setTemplate('gwas.html')
        studies = Study.all().fetch(10,0)
        self.out({'studies': studies})

class studyPresenter(AppRequestHandler):
    def get(self, i):
        self.setTemplate('study.html')
        studies = Study.gql("WHERE pubmed_id = :1", i).fetch(1,0)
        self.out({'studies': studies})

__routes__ = [('/gwas/', gwasReader),
              ('/study/(.*)', studyPresenter)]
