from pymongo import MongoClient


if __name__ == '__main__' :
    print('Hello World')
    m_conn = MongoClient('mongodb://{}/{}'.format('localhost:27017', 'demo'))
    mdb = m_conn.get_database('demo')
    m_coll = mdb.get_collection('hello')
    ins_result = m_coll.insert_one({"first-name": "AA", "last-name": "BB"})
    print(m_coll.find_one({'_id': ins_result.inserted_id}))
    del_result = m_coll.delete_one({'_id': ins_result.inserted_id})
    print(del_result.raw_result)
    print(m_coll.distinct('first-name'))
    m_conn.close()
