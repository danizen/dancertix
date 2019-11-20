# dancertix

## Summary

A web application to manage reservations of tickets to be purchased for dancers in young companies.

## NLM specific Sandbox automation

You may want to create the following git aliases, using appropriate values for _BUCKET_ and _PROFILE_:

```bash
git config alias.tarball "archive -o dancertix.tgz -- HEAD"
git config alias.upload "!aws s3 cp dancertix.tgz s3://BUCKET/python/projects/dancertix.tar.gz --profile=PROFILE"
```

Then, you will be able to promote the code in the sandbox as follows:

```bash
git tarball
git upload
```

## Heroku

On heroku, this application is deployed using both the python buildpack and the nodejs buildpack
