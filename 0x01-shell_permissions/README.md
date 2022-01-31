# WHAT DO THE SCRIPTS DO ? :octocat:


:one: The first script switches the current user to betty 0-iam_betty

:two: The second script prints the effective username of the current user : 1-who_am_i

:three: The third script prints all the groups the current user is part of : 2-groups

:four: The fourth script changes the owner of the file *hello* to the user *betty* : 3-new_owner

:five: The fifth script creates an empty file called *hello* : 4-empty

:six: The sixth script adds execute permission to the owner of the file *hello* : 5-execute

:seven: The seventh script adds execute permissions to the owner and the group owner, and read permissions to other usersn to the file *hello* : 6-multiple_permissions

:eight: The eight script adds execution permission to the owner, the group owner and the other usersn to the file *hello* : 7-everybody

:nine: The ninth script sets the permission to the file hello as follows :

* Owner : no permission at all
* Group : no permission at all
* Other users : all the permissions

:one::zero: The tenth script sets the mode of the file *hello* to this : 9-John_Doe
*-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello*

:one::one: The eleventh script sets the mode of the file hello the same as olleh's mode

*The file olleh will be in the working directory
*The file hello will be in the working directory

:one::two:The twelveth script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.Regular files should not be changed.
: 11-directories_permissions

:one::three:The thirteenth script creates a directory called dir_holberton with permissions 751 in the working directory : 12-directory_permissions

**ADVANCED

:one::zero::zero: The first script changes the owner to betty and the group owner to holberton for all the files and directories in the working directory : 100-change_owner_and_group

:one::zero::one:The second script changes the owner and the group owner of _hello to betty and holberton respectively.  The file _hello is in the working directory and is a symbolic link : 101-symbolic_link_permissions

:one::zero::two:The third script changes the owner of the file hello to betty only if it is owned by the user guillaume : 102-if_only

:one::zero::three:The fourth script will play the StarWars IV episode in the terminal : 103-star_wars

*************************************************************************************************************************************************************
> Powered by *fackfone* for ALX - HOLBERTON SOFTWARE ENGINEERING Cohort 3 June 2021
