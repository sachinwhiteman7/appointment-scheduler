# Appointment Scheduler

Appointment Scheduler project with Django Rest framework ready for Docker.

# Quickstart in Development

For setting up Appointment scheduler locally, clone the repo and checkout to main branch.
You must have
Latest docker version
Docker version 19 or greater

Latest Docker-compose version
docker-compose version 1.24.0 or greater

# API Documentation

Three APIs are available in the project.

##1. To create and list users.

   Two types of Users are available , Interviewer and Candidate, differentiated by 
   _user_type_ field in User model.

   GET request will provide the list of all users, both interviewers and candidates.
where POST method is used to create a User.  

```
http://localhost:8000/accounts/user/
```

use the above URL to create a user, username and password are the required fields.
user_type='candidate' will create a candidate and user_type='interviewer' will create an interviewer.
if no user_type is provided, user will be created as a interviewer.

## 2. Create Time slot and List timeslots.
timeslot have three fields. user field, which is a foreign key to user, start time and end time.
difference between end time and start time is always 1 hour.

```
http://localhost:8000/timeslots/
```

Above url is used to list timeslots with GET request, and create a timeslots with POST request.

## 3. API to get common time slots
  
this API after taking interviewer id and candidate id as input returns available common time slots.

```
http://localhost:8000/timeslots/common-slots/
```

#Answer to questions asked

### 1. Can you suggest a better solution to the above mentioned interview scheduling problem?
 
Ans : Instead of checking for a common available timeslots, It would be better to provide an
API that would list all the available slots for a interviewer so that the candidate can 
choose an appropriate slot. Thus reducing the complexity in the code and could avoid the HR too.

### 2. If you had some more time how would you improve your solution?

Ans : I could add date to timeslots, thus making the solution more clear and also the above mentioned solution.