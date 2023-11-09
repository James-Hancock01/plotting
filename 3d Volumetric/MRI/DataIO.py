import tempfile
import os
from urllib.request import urlretrieve
import zipfile
import nibabel
from skimage import io
import matplotlib.pyplot as plt
import shutil

d = None


def getData():

    # Create a temporary directory
    d = tempfile.mkdtemp()

    # Return the tail of the path
    os.path.basename('http://google.com/attention.zip')

    # Define URL
    url = 'http://www.fil.ion.ucl.ac.uk/spm/download/data/attention/attention.zip'

    # Retrieve the data
    fn, info = urlretrieve(url, os.path.join(d, 'attention.zip'))

    # Extract the contents into the temporary directory we created earlier
    zipfile.ZipFile(fn).extractall(path=d)

    # List first 10 files
    [f.filename for f in zipfile.ZipFile(fn).filelist[:10]]

    # Read the image 
    struct = nibabel.load(os.path.join(d, 'attention/structural/nsM00587_0002.hdr'))

    # Get a plain NumPy array, without all the metadata
    # struct_arr = struct.get_data()
    struct_arr = struct.get_fdata()

    struct_arr = io.imread("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/attention-mri.tif")

    # plt.imshow(struct_arr[75], aspect = 0.75)
    struct_arr2 = struct_arr.T
    # plt.imshow(struct_arr2[34])

    # plt.show()
    return struct_arr2

def cleanup():
    # Remove the temporary directory
    shutil.rmtree(d)