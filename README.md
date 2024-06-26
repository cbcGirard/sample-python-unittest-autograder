> CBCG modifications
> 
> Quasi-reasonable additions for testing `input`/`print`-based programs, spoofing stdin
> 
> Sub-class `lib_text_handler.TestText` for these cases
> 
> Initial attempts to install and use specific Python version for grading not yet successful, but should fail gracefully

# sample-python-unittest-autograder

A simple Gradescope autograder for Python based on `unittest` test cases.

This repo is designed to be used in conjunction with the 
[link-gs-zip-with-repo](https://github.com/ucsb-gradescope-tools/link-gs-zip-with-repo) tool.

The [link-gs-zip-with-repo](https://github.com/ucsb-gradescope-tools/link-gs-zip-with-repo)
allows you to easily link a Gradescope autograded assigment with a github repo.  You only have to create
the `Autograder.zip` file once; after that, you can make changes to the assignment simply by pushing them
to a github repo.

# Instructions

## Step 1: Clone this template

* Create a new empty private repo, e.g. with the name PRIVATE-cs8-s18-labxx-gs
* Clone the empty repo with `git clone <url>`
*  `cd` into that directory:
   > `cd PRIVATE-cs8-s18-labxx-gs`
* Add a remote for this sample repo via: 
   > `git remote add template git@github.com:ucsb-gradescope-tools/sample-python-unittest-autograder.git`
* Pull from this sample repo via `git pull template master`
* Push to origin with `git push origin master`

## Step 2: Edit the template for your assignment

* In `grade.sh` edit the environment variable `EXPECTED_FILES` to list the files you expect the student to submit.  Only these
   will be copied from the student submission into the space where the assignment is graded.
   
   If you prefer *all* files to be copied in, edit the `grade.sh` script to copy all files from `/autograder/submission` into
   the target directory.
   
* In EXECUTION-FILES, under the directory `tests`, edit the file given so that it contains the unit tests that you want to be used as a basis
   for the student's graded.   Use the decorators from the Gradescope 
   provided module 
   [autograder_utils](https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils).  (Quick reference below.)

   If converting from submit.cs, put any files that were under EXECUTION-FILES on submit.cs that are needed
   for your tests.

* Optional: If converting from submit.cs, if there are BUILD-FILES in the submit.cs solution, store them
   under BUILD-FILES.

## Step 3: Test your autograder locally (optional)

To test your autograder locally, try putting a correct sample solution
in the `SAMPLE-SOLUTION-1` directory and an incorrect sample solution in
the `SAMPLE-SOLUTION-2` directory.  (You have the option of creating
additional `SAMPLE-SOLUTION-nn` directories, as few or as many as you
see fit if you want to test a wider range of solution possibilities.)

To check what will happen, run:
* `./grade.sh SAMPLE-SOLUTION-1`
* `./grade.sh SAMPLE-SOLUTION-2` 
* etc.



(When converting assignments from UCSB's submit.cs, you might adapt a "perfect" solution and a "flawed" solution from among previous student submissions, by looking at the grade assigned by submit.cs.)

In each case, look at the file `MAKE-STUDENT-OUTPUT/results.json` to see whether it reflects what you expect the resulting grade to be.   

## Step 4: Create an `Autograder.zip` using the [link-gs-zip-with-repo](https://github.com/ucsb-gradescope-tools/link-gs-zip-with-repo) tool.
   
* Clone the [link-gs-zip-with-repo](https://github.com/ucsb-gradescope-tools/link-gs-zip-with-repo).
* In that repo, edit `env.sh` to point to your repo.  You don't need to commit that change.
* Run the script `./make_deploy_keys.sh` and upload your deploy key to the new repo you created for your assignment.
* Run the script `./make_autograder_zip.sh` and then upload the `Autograder.zip` to Gradescope.

You are now ready to test your autograded assignment.
   
# Decorator reference

As quick reference, here are examples of the decorators you can use on `unittest` tests:
   
* `@weight(5.0)` (parameter is of type float; represents number of points)
* `@
* `@tags("conditionals", "recursion")` (parameters are strings)
* `@visibility("after_due_date")` Legal values are explained [in Gradescope's documentation](https://gradescope-autograders.readthedocs.io/en/latest/specs/#controlling-test-case-visibility)
   * `"hidden"`
   * `"after_due_date"`
   * `"after_published"`
   * `"visible"` (default).  
   
   
