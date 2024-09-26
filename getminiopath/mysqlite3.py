import sqlite3
import time

class MinioDatabase:
    def __init__(self, db_name='minio.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                path TEXT PRIMARY KEY,
                timestamp BIGINT
            )
        """)
        self.conn.commit()

    def insert_file(self, file_path, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        self.cursor.execute("INSERT INTO files (path, timestamp) VALUES (?, ?)", (file_path, timestamp))
        self.conn.commit()

    def get_file(self, file_path):
        self.cursor.execute("SELECT * FROM files WHERE path = ?", (file_path,))
        return self.cursor.fetchone()

    def update_file_timestamp(self, file_path, new_timestamp):
        self.cursor.execute("UPDATE files SET timestamp = ? WHERE path = ?", (new_timestamp, file_path))
        self.conn.commit()

    def delete_file(self, file_path):
        self.cursor.execute("DELETE FROM files WHERE path = ?", (file_path,))
        self.conn.commit()


# 使用示例
with MinioDatabase() as db:
    # 插入文件记录
    db.insert_file('/path/to/file')

    # 查询文件记录
    file_info = db.get_file('/path/to/file')
    print(file_info)

    # 更新文件时间戳
    new_timestamp = int(time.time())
    db.update_file_timestamp('/path/to/file', new_timestamp)

    # 删除文件记录
    db.delete_file('/path/to/file')

# 此处程序退出，不论是否有异常，数据库连接都会自动关闭