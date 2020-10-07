= Git

== Everyday we are googling....

    * Get the commit before file deletion
    git rev-list -n 1 HEAD -- <file_path>

    * the ^ is important
    git checkout <commit>^ -- <file_path>
