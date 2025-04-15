import unittest
import naukri
import os
import io
from pypdf import PdfReader, PdfWriter


class Test(unittest.TestCase):
    def test_naukri(self):
        (status, driver) = naukri.naukriLogin(headless=True)
        naukri.tearDown(driver)
        self.assertFalse(status)

    
    def test_update_resume(self):
        originalResumePath = naukri.originalResumePath
        modifiedResumePath = naukri.modifiedResumePath

        # Create a simple PDF file
        packet = io.BytesIO()
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(originalResumePath, "wb") as f:
            writer.write(f)

        result_path = naukri.UpdateResume()
        # Check if the modified PDF file is created
        self.assertTrue(os.path.exists(result_path))
        self.assertEqual(result_path, modifiedResumePath)



if __name__ == "__main__":
    unittest.main()
