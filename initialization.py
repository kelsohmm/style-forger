from CameraImageStream import CameraImageStream
from TransformedImageStream import TransformedImageStream
import config
import Mocks
from facebook_upload import fb
from chainer_fast_neuralstyle.TransformationApplier import TransformationApplier


def initializeImageStreams(root):
    if config.MOCK_TRANSFORMATION_APPLIER:
        transformationApplier = Mocks.TransformationApplierMock(1)
    else:
        transformationApplier = TransformationApplier()

    if config.MOCK_FACEBOOK_UPLOAD:
        afterTransformationAction = Mocks.afterTransformationActionMock
    else:
        afterTransformationAction = fb.upload_file

    cameraImageStream = CameraImageStream()
    transformedImageStream = TransformedImageStream(root, cameraImageStream, transformationApplier, afterTransformationAction)

    return cameraImageStream, transformedImageStream
