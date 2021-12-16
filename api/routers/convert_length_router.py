from fastapi import APIRouter, Depends


router = APIRouter()

@router.post("/calculators/convert_length", tags=["unit conversion"], summary="Converts different units of length")
def convert_length_http(request: dict):

    """
    # Description
    This endpoint will convert length (**length**) expressed in one or more common unit types to several other common unit types.

    ## Request
    This endpoint accepts a JSON object.
    - **length**: Accepts a JSON array containing one or multiple JSON objects:
        - *unit*:  Accepts the following units as strings: 'mm' (millimetre), 'cm' (centimetre), 'm' (metre), 'km' (kilometre), 'in' (inch) and 'ft' (foot). 
        - *value*: Accepts a value of length as float. 
    
    One or multiple *unit\\value* JSON objects must be added as a JSON array to the request body. If multiple *unit\\value* objects (differing unit types are allowed) are added then these will then be summed and converted.
    This is useful when for example combining 'ft' and 'in'.

    ## Response
    This endpoint will return a response body as a JSON object with the following values as floats.
    - **mm**: millimetre
    - **cm**: centimetre
    - **m**: metre
    - **km**: kilometre
    - **in**: inch
    - **ft**: foot
    - **ft_in**: height split into foot and inch.
    - **m_cm**: height split into metre and centimetre.
    """

    pass