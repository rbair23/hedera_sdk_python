from hedera_sdk_python.hapi import basic_types_pb2

class TopicId:
    def __init__(self, shard=0, realm=0, num=0):
        self.shard = shard
        self.realm = realm
        self.num = num

    @classmethod
    def from_proto(cls, topic_id_proto: basic_types_pb2.TopicID):
        """
        Creates a TopicId instance from a protobuf TopicID object.
        """
        return cls(
            shard=topic_id_proto.shardNum,
            realm=topic_id_proto.realmNum,
            num=topic_id_proto.topicNum
        )

    def to_proto(self):
        """
        Converts the TopicId instance to a protobuf TopicID object.
        """
        topic_id_proto = basic_types_pb2.TopicID()
        topic_id_proto.shardNum = self.shard
        topic_id_proto.realmNum = self.realm
        topic_id_proto.topicNum = self.num
        return topic_id_proto

    def __str__(self):
        """
        Returns the string representation of the TopicId in the format 'shard.realm.num'.
        """
        return f"{self.shard}.{self.realm}.{self.num}"

    @classmethod
    def from_string(cls, topic_id_str):
        """
        Parses a string in the format 'shard.realm.num' to create a TopicId instance.
        """
        parts = topic_id_str.strip().split('.')
        if len(parts) != 3:
            raise ValueError("Invalid TopicId format. Expected 'shard.realm.num'")
        return cls(shard=int(parts[0]), realm=int(parts[1]), num=int(parts[2]))