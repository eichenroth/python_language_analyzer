import ast

from python_language_analyzer.detection import Detection, ClassDetection, FunctionDetection
from python_language_analyzer.detector import Detector


class ClassDetector(Detector):
    def __call__(self):
        file_module = ast.parse(''.join(self.file))
        class_visitor = ClassVisitor()
        class_visitor.visit(file_module)

        return [detection for detection in class_visitor.detections if detection.DETECTION_NAME == 'class']


class ClassVisitor(ast.NodeVisitor):
    def __init__(self):
        self._object_stack = []
        self.detections = []

    def generic_visit(self, node, detection=None):
        if detection is None:
            detection = Detection()

        if hasattr(node, 'lineno'):
            detection.begin = node.lineno

        self._object_stack.append(detection)

        super().generic_visit(node)

        self._object_stack.pop()

        if len(self._object_stack) > 0:
            self._object_stack[-1].add_child(detection)
        else:
            self.detections.append(detection)

    def visit_ClassDef(self, node):
        detection = ClassDetection()
        self.generic_visit(node, detection)

        detection['name'] = node.name

        method_number = 0
        for child_detection in detection.children:
            if child_detection.DETECTION_NAME == 'function':
                method_number += 1
        detection['method_number'] = method_number

    def visit_FunctionDef(self, node):
        detection = FunctionDetection()
        self.generic_visit(node, detection)

    def visit_Module(self, node):
        super().generic_visit(node)
