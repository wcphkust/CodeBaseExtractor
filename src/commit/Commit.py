class Commit:
    commit_id = None
    commit_time = None
    author_id = None

    def commit(self, p_commit_id, p_commit_time, p_author_id):
        self.commit_id = p_commit_id
        self.commit_time = p_commit_time
        self.author_id = p_author_id

