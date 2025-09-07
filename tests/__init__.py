



import warnings



try:

    from urllib3.exceptions import SNIMissingWarning



                                                             

                                                      

                                                                

    warnings.simplefilter("always", SNIMissingWarning)

except ImportError:

                                                             

    SNIMissingWarning = None

