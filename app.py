from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pandas as pd

import spacy
import docx2txt
import PyPDF2
from glob import glob
import pickle

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)


filename = "C:/Users/Rohit Chavan/Resume_Project-main/resume1_model.pkl"
model = pickle.load(open(filename, 'rb'))
tfidf_vectorizer=pickle.load(open('transform.pkl','rb'))


#model.predict()  
def extract_text_from_doc(doc_path):
    temp = docx2txt.process(doc_path)
    text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    return ' '.join(text)
def extract_skills(resume_text):
    nlp = spacy.load('en_core_web_sm')
    nlp_text = nlp(resume_text)

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    
    # reading the csv file
    #data = pd.read_csv("skills.csv") 
    
    # extract values
    
    
    skills=['github', 'material ui', 'mac xcode', 'sqr', ' xmlp', 'change deduction', 'java', 'ansible', 'js', 'c-language', 'react.js', 'hp-ux', 'tuxedo', 'sass', 'isolation levels', 'trending', 'responsive designs', 'framework7', 'web logic', 'pandas', 'crystal reports', 'ms sql server', 'bootstrap', 'integrations-eib', 'scalacore java', 'winscp', 'framework', 'python', 'reporting and integrations', ' sql', 'resource management', 'jira', ' sql server', 'javascript', 'javascript', 'php', ' x-path', 'peoplecode', 'billing', 'ps security', 'linux', 'tuxedo', 'unix sql server management   studio (ssms)', 'eib', 'rstudio', 'web technologies', 'javafullstackdevelopment', 'visual studio', 'pia', 'c++', 'picof and workday studio', 'webpage optimization', 'cobol software', 'sdlc', 'webpage designing', 'ecma', 'ms-outlook', 'photoshop', 'peoplesoft tools', 'time tracking', 'component interface', 'responsive design', 'putty', 'java script', 'template designs', 'app designer', 'sqr package', 'mobile website', 'ap', 'people code', 'integrations eib', 'calculated fields', 'windows administration', '11i', 'talend', 'notepad++', 'aws', 'winscp', 'node js', 'share point', 'windows 7.0', 'foundation framework', 'erp', 'exceltocl', 'core java', 'css3/bootstrap', 'hrms', 'mac', 'business processes', 'purchase', 'api', 'workday', 'ssis', 'windows 7', 'visual studio code', 'front-end architecture', 'data analytics', 'people soft applications', 'razorsql', 'inventory', 'css', 'java', 'sql server profiler', 'ses', 'sass', 'json', 'xml publisher', 'pig', 'reportwriting', 'ms office suite (excel, word, notepad)', 'photoshop cs6', 'peoplesoft', 'jira', 'mariadb', 'sqoop', 'saga', 'web server domain', 'cloning', 'jenkins', 'c', 'gl', 'json', 'react frameworks', 'benefits', 'maestro', 'spa', 'workday studio', 'cte', 'service now', 'data warehouse (dwh)', 'heidisql', 'waf', 'bootstrap framework', 'feature designing', 'centos', 'sql server reporting services (ssrs)', 'reports', 'pum', 'workday studio', 'alerts', 'ssl', 'workday hcm', 'requisition', 'business intelligence (bi)', 'json', 'application designing', 'elm', 'spoon', 'benefits and absence management', 'report writer', 'angular 10', 'netbeans', 'sysaudit', 'process scheduler', 'dom functions', 'integration broker', 'htmlcss3', 'db solo', 'phire', 'compensation', 'rds', 'mern stack', 'teradata', 'apache', 'react js', 'studio', 'rdbms', 'exchanger xml tool', 'cte', 'unix', 'core connectors', 'ms visual studio 2013', 'e-procurement', 'c', ' odyssey jira', 'microservices', 'db2', 'odyssey dashboard', 'ms-sql', 'document transformation', 'administration', 'w3c standards', 'project delivery', 'react hooks', 'dml', 'core connectors picof', 'devops', 'shell scripts', 'composite', 'birt', 'visual studio code (vscode)', 'numpy', 'windows 10', 'microsoft powerpoint', 'ms office 365', 'bip', 'etl tool - ssis', 'unix', 'workday web services', 'control m', 'react', 'peoplesoft campus application upgrade', 'machine learning', 'account payable', 'advance', 'xml', 'url routing', 'jquery', 'mongodb', 'sql server integration services (ssis)', 'javascript', 'business objectswindows', 'ddl', 'node js', 'web services (wsdl & soap)', 'bootstrap', 'mysql', 'data migration', 'web services', 'mysql', 'web services', 'pentaho data integration (etl)', 'sqr', 'excel,sybase ase 15.7 server', 'core hr', 'purchase order', 'bootstrap', 'people code', 'microsoft excel', 'cloud platform - aws redshift', 'xhtml', 'complex stored procedures', 'peoplesoft security', 'windows 2008 server', 'spring boot', 'windows xp', 'peoplesoft', 'peopletools', 'css', 'tools configuration', 'ranking functions', 'wireframe and design pattern translation', 'integrationbroker', 'web services soap & rest', 'document transformer', 'core connector', 'windows xp/ 7', 'file layout', 'jquery mobile themes', 'react.js', 'sql server', 'tableau', ' mvel web services soap & rest', 'hbase', 'windows server 2008', 'oracle 11g', 'sql server 2017', 'peoplesoft administration', 'client surviving', 'sas', 'dba', 'css3', 'windows 8', 'sql', 'rman configuation', 'domain security', 'github', 'xml publisher', 'concurrency', 'appworx', 'sub queries', 'ar', 'dt', 'dell sonic global vpn client', 'joins', 'windows7/xp', 'data pump', 'matplotlib', 'ms sql server', 'python', 'rac', 'agile', 'bi publisher', 'integration', 'eib inbound/outbound', 'mysql', 'html', 'nestjs', 'absence management', 'performance improvement', 'ms office', 'html5', 'oracle 10g', 'html 4', 'sql server 2008', 'html5', 'athena', 'windows xp/windows 7', 'mvel', 'document object model (dom) layout', 'node.js', 'jquery', 'set operators', 'bit bucket', 'dreamweaver cs6', 'winscp', 'pl/sql-oracle', 'maintenance', 'jquery', 'x-path', 'bootstrap', 'application engine', 'exceltoci', 'sqlserver 2014 2016databases', 'linux', 'soap', 'rhel', 'informatica', 'microsoft oﬃce suite', 'angular', 'ubuntu', 'microsoft word', 'awe', 'ssms', 'microsoft office', 'mongo database', 'constraints', 'https', 'basic studio', 'html 5', 'edit plus', 'ib', 'redux', 'git', 'hive', 'thunk', 'oracle', 'birt', 'creating and handling http crud', 'sup orgs', 'debugging', 'es6', 'peopletools upgrade', 'reactjs', 'crm', 'sql', 'vendor management', 'basic shell scripting,informatica 9 &10', 'weblogic', 'windows', 'mac os', 'aws/azure', 'application package', 'vmware workstation', 'unix', 'ptf', 'ci', 'xml', 'wordpress framework', 'data mover', 'reactjs', 'responsive', 'power bi', 't-sql', 't-sql', 'hooks', 'sql server management studio', 'ms-dos', 'simple', 'react js', 'eclipse', 'r', 'procurement', 'illustrator cs6', 'html', 'dddaudit', 'xslt', 'hcm', 'user defined functions', 'react.js', 'coding', 'docker', 'transporter', 'ui designing', 'application designer', 'database triggers', 'sql developer', 'report writer', 'shell scripting', 'type script', 'workday security configuration', 'sql server 2012', 'iloads', 'bea tuxedo 8.1', 'calculated fields', 'react js', 'javascript', 'tcl', 'visio', 'ssms', 'express js', 'ps query', 'studio, core connectors', 'core hcm', 'po', 'xslt & studio', 'xampp', 'studio ide', 'pum', 'matrix', 'business process', 'dashboards', 'constraints', 'coreldraw x5', 'security', 'dbms', 'iws', 'vs code', 'microsoft visual studios', 'alteraudit', 'ps query', 'oracle', 'windows,sql developer', 'designs/development', 'notifications', 'xsd', 'data guard', 'fscm', 'staffing and compensation', 'impla', 'ci.xml']
    
    skillset = []
    
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        #print(token)
        if token in skills:
          skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]        


def model_predict(resume_path, model):
    if(resume_path.endswith('docx')):
        text=extract_text_from_doc(resume_path)
        skills=' '.join(extract_skills(text))
        # Preprocessing the image
        x = tfidf_vectorizer.transform(pd.Series(skills)).toarray()
        preds = model.predict(x)
        return preds
    if(resume_path.endswith('pdf')):
        pdfreader=PyPDF2.PdfFileReader(resume_path)
        x=pdfreader.numPages
        pageobj=pdfreader.getPage(x-1)
        text=pageobj.extractText()
        skills=' '.join(extract_skills(text))
        # Preprocessing the image
        x = tfidf_vectorizer.transform(pd.Series(skills)).toarray()
        preds = model.predict(x)
        return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        if(preds==0):
            result='Designation is SQL Developer'
        elif(preds==1):
            result='Designation is peoplesoft'
        elif(preds==2):
            result='Designation is React Developer '
        elif(preds==3):
            result='Designation is Workday'


              # Convert to string
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)

