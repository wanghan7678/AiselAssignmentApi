# AiselAssignmentApi

It implemented the endpoints:

POST ~/api/token/obtain/
POST ~/api/token/refresh/
POST ~/api/user/login/
POST ~/api/user/registration/
POST ~/api/user/all/
POST or GET~/api/patients/all
POST or GET ~/api/patients/get
POST ~/api/patients/update
POST or DELETE ~/api/patients/delete
POST ~/api/patients/new

The endpoints:
~/api/user/all/
~/api/patients/all
~/api/patients/get
~/api/patients/update
~/api/patients/delete
~/api/patients/new

are under authentication. Only requests with valid tokens can successfully access them.

The delete end point is not really deleted.  It only hides the deleted patients, so we can  easily implement an undo.

When the user try to login: POST to ~/api/user/login/, it will give an access and refresh token.
