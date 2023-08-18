from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def find_object_by_id(object_id, array):
        for obj in array:
            if obj.id == object_id:
                return obj

    def add_category(self, category: Category):
        if category.id not in [c.id for c in self.categories]:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic.id not in [t.id for t in self.topics]:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document.id not in [d.id for d in self.documents]:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_object_by_id(category_id, self.categories)
        if category:
            category.edit(new_name)

    def delete_category(self, category_id):
        category = self.find_object_by_id(category_id, self.categories)
        if category:
            self.categories.remove(category)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_object_by_id(topic_id, self.topics)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def delete_topic(self, topic_id):
        topic = self.find_object_by_id(topic_id, self.topics)
        if topic:
            self.topics.remove(topic)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_object_by_id(document_id, self.documents)
        if document:
            document.edit(new_file_name)

    def delete_document(self, document_id):
        document = self.find_object_by_id(document_id, self.documents)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        return self.find_object_by_id(document_id, self.documents)

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += doc.__repr__()
        return result
