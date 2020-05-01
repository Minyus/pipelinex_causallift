def get_sim_data(parameters):
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
    from causallift import generate_data

    seed = parameters.get("seed")

    df = generate_data(
        N=1000,
        n_features=3,
        beta=[0, -2, 3, -5],  # Effect of [intercept and features] on outcome
        error_std=0.1,
        tau=[1, -5, -5, 10],  # Effect of [intercept and features] on treated outcome
        tau_std=0.1,
        discrete_outcome=True,
        seed=seed,
        feature_effect=0,  # Effect of beta on treated outxome
        propensity_coef=[
            0,
            -1,
            1,
            -1,
        ],  # Effect of [intercept and features] on propensity log-odds for treatment
        index_name="index",
    )

    return df
