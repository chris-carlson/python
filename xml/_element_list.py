class ElementList(list):

    def find_by_name(self, name):
        filtered_items = self.filter_by_name(name)
        if len(filtered_items) == 0:
            raise ValueError('Could not find a child with name \'' + name + '\'')
        elif len(filtered_items) > 1:
            raise ValueError('Found multiple children with name \'' + name + '\'')
        return filtered_items[0]

    def filter_by_name(self, name):
        return ElementList([item for item in self if item.name == name])

    def find_by_attribute(self, name, value):
        filtered_items = self.filter_by_attribute(name, value)
        if len(filtered_items) == 0:
            raise ValueError('Could not find a child with attribute \'' + name + '\' and value \'' + value + '\'')
        elif len(filtered_items) > 1:
            raise ValueError('Found multiple children with attribute \'' + name + '\' and value \'' + value + '\'')
        return filtered_items[0]

    def filter_by_attribute(self, name, value):
        return ElementList([item for item in self if name in item.attributes and item.attributes[name] == value])

    def find_by_data(self, data):
        filtered_items = self.filter_by_data(data)
        if len(filtered_items) == 0:
            raise ValueError('Could not find a child with data \'' + data + '\'')
        elif len(filtered_items) > 1:
            raise ValueError('Found multiple children with data \'' + data + '\'')
        return filtered_items[0]

    def filter_by_data(self, data):
        return ElementList([item for item in self if item.data == data])