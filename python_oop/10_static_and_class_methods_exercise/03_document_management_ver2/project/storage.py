from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if not self.__find_element_by_attr_name("name", category.name, self.categories):
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if not self.__find_element_by_attr_name("topic", topic.topic, self.topics):
            self.topics.append(topic)

    def add_document(self, document: Document):
        if not self.__find_element_by_attr_name("id", document.id, self.documents):
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_element_by_attr_name("id", category_id, self.categories)
        category.name = new_name if category else None

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_element_by_attr_name("id", topic_id, self.topics)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_element_by_attr_name("id", document_id, self.documents)
        document.file_name = new_file_name if document else None

    def delete_category(self, category_id):
        category = self.__find_element_by_attr_name("id", category_id, self.categories)
        self.categories.remove(category) if category else None

    def delete_topic(self, topic_id):
        topic = self.__find_element_by_attr_name("id", topic_id, self.topics)
        self.topics.remove(topic) if topic else None

    def delete_document(self, document_id):
        document = self.__find_element_by_attr_name("id", document_id, self.documents)
        self.documents.remove(document) if document else None

    def get_document(self, document_id):
        return self.__find_element_by_attr_name("id", document_id, self.documents)

    def __repr__(self):
        result = []
        [result.append(str(d)) for d in self.documents]
        return "\n".join(result)

    # HELPERS
    @staticmethod
    def __find_element_by_attr_name(attr, value, collection):
        return next((e for e in collection if getattr(e, attr, None) == value), None)
