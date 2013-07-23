## Ubuntu Edge Image

This handy Python script generates an image displaying the percentage of funds raised for the [Ubuntu Edge crowdfunding project](http://www.indiegogo.com/projects/ubuntu-edge). The entire script is written in Python and requires that the following Ubuntu packages be installed:

 - `python-lxml`
 - `python-imaging`

The script is executable and can be run simply with:

    ./update.py

By default, this will generate a file named `percentage.png` in the current directory. If you wish to have the image stored somewhere else, you can specify the directory via the `--directory` argument.

### Regular Intervals

The script can be set to run continuously, updating the image at regular intervals. To do this, simply invoke the script as follows:

    ./update.py --interval 30

This will cause the script to update the image every 30 minutes.