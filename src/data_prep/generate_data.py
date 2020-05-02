from causallift import generate_data


def generate_data_(params):
    """
    # Generate simulated data
    # "Sleeping dogs" (a.k.a. "do-not-disturb"; people who will "buy" if not
    treated but will not "buy" if treated) can be simulated by negative values
    in tau parameter.
    # Observational data which includes confounding can be simulated by
    non-zero values in propensity_coef parameter.
    # A/B Test (RCT) with a 50:50 split can be simulated by all-zeros values
    in propensity_coef parameter (default).
    # The first element in each list parameter specifies the intercept.
    """

    df = generate_data(**params)
    return df
