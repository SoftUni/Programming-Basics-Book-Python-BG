REM npm install -g gitbook-cli

rmdir /s /q _book

call gitbook install

call gitbook build . --log=debug --debug

git clone https://github.com/SoftUni/Programming-Basics-Book-Python-BG -b gh-pages gh-pages

xcopy /s /y _book gh-pages

cd gh-pages

git add .

git status

git commit -m "Book web site deployment"

git push

pause
