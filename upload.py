import git

def upload(repo, timestamp):
    print("Uploading...")

    repo.git.add(".")
    repo.git.commit(m="Changes detected at " + str(timestamp))
    repo.git.push()