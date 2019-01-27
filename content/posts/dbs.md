Title: Tale of two databases
Date: 2017-09-28
Summary: This post describes my struggle with a task to get data difference between two databases. The winning solution was to use SQL-Workbench/J software that has tons of quality settings to do not only data diff by way more complex stuff.

This post describes my struggle with a task to get data difference between two databases. The winning solution was to use SQL-Workbench/J software that has tons of quality settings to do not only data diff by way more complex stuff.

## Prequel

Today I have not an easy task. After an unsuccessful update script, the production database was acting weird. Some records were duplicated, some have corrupted data.

This error was not spotted fast enough, the production database contains new records, so decision was made to use fixtures for lost data. But it didn’t work well because of unique constraint on the table.

Also, there was hard to spot which table it was. We can see that something wrong, but original cause of this was ephemeral. Why is this? Legacy code and sloppy naming conventions. One of the models was named like `StudyPlanSubjectVariantPhaseBase`. That’s a long name, and you try to guess what it means.

So I was looking for some software that can make diff report about data in two databases and also generate SQL script so we can run it for production database to recover lost data.

After googling some answers on «stack overflow» was obvious that people mostly talking about database schema diff, and not about database data diff.

Luckily after researching deeper, I found an amazing piece of software called SQL Workbench/J. The interface and documentation are not great, but it is a powerful tool, that helped me solve an issue with production data.

## SQL Workbench/J

The first obstacle that I encounter was with database driver. Our database is running on **PostgreSQL** and when you selecting this database from the menu, the program is happily telling you that it has no idea where this database driver is. And error also makes a little sense `org.postgresql.Driver not found`.

After some time, I understand that I need to download a `*.jar` file from this site https://jdbc.postgresql.org/download.html, and manually tell SQL-Workbench/J to look at this file, take wherever it needs and keep calm.

Next steps are easy. You fill information about you database whereabouts (also I did not find if workbench can work with dumps or only real databases), host, port, user, pass e.t.c.

I encourage you to fill two databases (called «profiles» for some reason) at once while on setup step. Choose any profile and click «ok» and we are in the main window of the program.

It is not straightforward, but you need to write a special pseudo-SQL command to fire the diff process. No buttons or windows provided (it is not a bad thing, though).

I will provide a simplified example of a command that I used to the generate report:

    WbDataDiff -type=sql
               -referenceProfile=old_db
               -excludeTables=auth_user,django_migartions
               -ignoreColumns=created,modified
               -includeDelete=true
               -file=result_folder/result.sql;

A few important notes:
+ **type** is required
+ **ignoreColumns** can help distinguish important changes from timestamps updates
+ I encourage to provide **file** argument with a folder because otherwise your current working directory will be polluted with `*.sql` files

## Resume

I was impressed by the speed and accuracy of this program and highly recommend it for all sorts of database manipulation and analyze.
