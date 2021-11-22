# git bisect Demo repo

Simple "fizzbuzz" project to demonstrate how to use `git bisect`.

## How to use `git bisect`

Start the git bisect session and mark the good/bad commits

    git checkout main
    ## copy the test file (git will remove the file so you need an untracked copy)
    cp bisect_tests.example.py bisect_tests.py
    git bisect start
    git bisect bad
    git bisect good 32558cc

With an active bisect session you can now start testing

    ## Run the tests
    python bisect_tests.py

Any time the tests fail run `git bisect bad` and anytime the tests pass run `git
bisect good`. Eventually you should find the first bad commit.

## How to run the `git bisect run` demo

    ./set_bisect.sh
    git bisect run ./bisect_test.sh

After running the above commands you should be checked out to the bad commit.

NOTE: Two new files are created for this demo. Git deletes any tracked files as
it checks out commits so the test script and python tests need to be untracked
to work

## Run the slides in your browser (using reveal.js)

    cd slides
    python3 -m http.server
    ## OR
    python -m SimpleHTTPServer

See the slides at http://localhost:8000 (if python is not installed you can use
your favorite [static server one-liner command](https://gist.github.com/willurd/5720255))
