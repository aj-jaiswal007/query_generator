# Query Generator

Query Generator is a mini module to generate SQL and Mongo text search queries from simple AND | OR search expressions.
## For example
You have a DB table named **Resume**
In that table there is a column name **raw_content**
And you want to filter those resumes which have the words **python** OR **java** in it.

So your search string will be in that case
```
python OR java
```
This will generate the following SQL and MongoDB queries:
```
MONGO FILTER QUERY:
{'$or': [{'raw_content': {'$regex': 'python', '$options': 'i'}}, {'raw_content': {'$regex': 'java', '$options': 'i'}}]}


SQL QUERY:
SELECT * FROM "Resume" WHERE ("Resume"."raw_content" iLIKE %python% OR "Resume"."raw_content" iLIKE %java%) ;
```

# How to test

- Clone the respository
- Run command `python3 main.py test` to run pre-defined test cases
- Run command `python3 main.py` to test query generator for multiple custom inputs