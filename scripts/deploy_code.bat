mkdir ..\upload\

xcopy /s ..\lambda\* ..\upload\

pipenv lock -r > ../upload/requirements.txt

pip install -r ../upload/requirements.txt -t ../upload/

del ../upload/requirements.txt

"C:\Program Files\7-Zip\7z.exe" a -tzip "..\upload\lambda.zip" ..\upload\*

aws lambda update-function-code --function-name FUNCTION:ARN --zip ..\upload\lambda.zip

rd /s /q ..\upload\