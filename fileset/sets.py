import os

from ruamel.yaml.comments import CommentedMap, CommentedSeq

from .exceptions import FileSetException

SETS_PROPERTIES = ['sets']


class FileSet():

    def __init__(self, name):
        self._name = name
        self._sets = []
        self._assets = []

    @property
    def name(self):
        return self._name

    @property
    def assets(self):
        return self._assets

    @property
    def sets(self):
        return self._sets

    @property
    def all_assets(self):
        result = []
        for s in self.all_sets:
            result += s.assets
        return sorted(set(result))

    @property
    def all_sets(self):
        result = [self]
        for s in self._sets:
            for subset in s.all_sets:
                if subset not in result:
                    result.append(subset)
        return result

    def add_set(self, s):
        self._sets.append(s)

    def add_sets(self, sets):
        self._sets += sets

    def add_asset(self, a):
        self._assets.append(a)

    def add_assets(self, assets):
        self._assets += assets

    def print_paths(self, stream, prefix=''):
        current_path = os.path.join(prefix, self.name)
        print(current_path, file=stream)
        for a in self.assets:
            print(os.path.join(current_path, str(a)))
        for s in self.sets:
            s.print_paths(stream, current_path)

    def print_asset_paths(self, stream, prefix=''):
        current_path = os.path.join(prefix, self.name)
        for a in self.assets:
            print(os.path.join(current_path, str(a)))
        for s in self.sets:
            s.print_asset_paths(stream, current_path)


class FileSetFactory():

    def create_filesets(self, raw_sets):
        result = []
        for set_name in list(raw_sets):
            fs = FileSet(set_name)
            subsection = raw_sets[set_name]
            if isinstance(subsection, (CommentedMap, dict)):
                fs.add_sets(self.create_filesets(subsection))
            elif isinstance(subsection, (CommentedSeq, list)):
                fs.add_assets(subsection)
            else:
                raise FileSetException(f'Unknown subsection type {str(type(subsection))} for {set_name}')
            result.append(fs)
        return result


class RawFactory():

    def create_filesets(self, filesets):
        return {'sets': {s.name: self.create_fileset(s) for s in filesets}}

    def create_fileset(self, fileset):
        if fileset.assets:
            return fileset.assets
        else:
            return {s.name: self.create_fileset(s) for s in fileset.sets}


def print_sets_as_paths(filesets, stream):
    for fs in filesets:
        fs.print_paths(stream)


def print_assets_as_paths(filesets, stream):
    for fs in filesets:
        fs.print_asset_paths(stream)
