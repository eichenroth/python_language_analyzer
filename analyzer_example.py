from python_language_analyzer.analyzer import Analyzer
from python_language_analyzer.detectors.built_in_function_detector import BuiltInFunctionDetector
from python_language_analyzer.detectors.class_detector import ClassDetector
from python_language_analyzer.detectors.control_flow_detector import ControlFlowDetector


def main():
    file_name = './jupyter/files/hierarchical_softmax.py'
    #file_name = './jupyter/files/multiple_inheritances.py'

    with open(file_name, 'r') as f:
        file = f.readlines()

    detectors = [ClassDetector]
    analyzer = Analyzer(file, detectors)

    detections = analyzer()
    print(detections)


if __name__ == '__main__':
    main()
