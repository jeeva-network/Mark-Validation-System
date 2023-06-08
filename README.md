# Mark Validation System



## Need to download 

 - [Download-Python](https://www.python.org/downloads/)

 ## Type into the cmd

Make sure Python is installed on your Windows or Linux

```bash
  python --version
```

Make sure Python is installed on your MacOs

```bash
  python -version
```

 
 ## About the Project
 
This project is used to validate the student's passing and failing mark in the subject.


![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/first.png)

## Condition

This only supports the number without special characters and white space.If you give only a number in the UG/PG input field you get the result.

Number=1234567890

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/nummber(support).png)


## Not support

Specialcharacter=!@#$%^&*()-_+=:;"'<>,.?/~...etc

If either one of the input fields gives a string or white space it will show this warning message to recheck or enter a valid mark in the particular UG/PG input field.

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/special(notsupporting).png)

## or

If either one of the input fields or all the input fields you doesn't give a value this will show a warning message to fill out the all-input fields.

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/filloutall.png)

## Condition Value

### UG

UG-CIA=15-50\
UG-EOS=20-50\
UG-Total=40

If either one of the input fields or both input fields in UG gives less than the minimum condition value you fail to be in the particular subject or both. the previous two conditions are satisfied, but if you are not satisfied with the total condition you will get a fail message.

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/ugvalid.png)

If either one of the input fields or both input fields in UG gives more than the maximum condition value you will get the warning message to enter a valid mark in the particular subject or both subjects.

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/ugnotvalid.png)

### PG

PG-CIA=20-50\
PG-EOS=25-50\
PG-Total=50

If either one of the input fields or both input fields in PG gives less than the minimum condition value you fail to be in the particular subject or both. the previous two conditions are satisfied, but if you are not satisfied with the total condition you will get a fail message.

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/pgvalid.png)

If either one of the input fields or both input fields in PG gives more than the maximum condition value you will get the warning message to enter a valid mark in the particular subject or both subjects.

![App Screenshot](https://github.com/jeeva-network/mark-validation-python/blob/main/pgnotvalid.png)


## 🚀 About Me

I am a passionate learner of Python and Web Development. I have honed my skills through various online courses and personal projects. I am well-versed in Python programming concepts and have a strong understanding of MERN stack Web Development. I am confident in my ability to create responsive and visually appealing web pages using these technologies. My goal is to continue to grow and develop my skills in the tech industry and contribute to the development of innovative solutions.
