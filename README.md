# CanardExplosionResearch_CompNeuroScience_CSM

Colton Koenig and Daniel Krawciw

## Our Goals

We are researching Canard Explosions in our Computational Neuroscience class final project. This Repository contains tests and functions for our results.

1. Have functions/files together to compute solutions to 2D Reduced HH and FH-N models that include the applied current specified in Börgers

2. Work to find parameter range to make Canard Explosions

3. Obtain information on dynamics when the Neuron exhibits Canard behavior

4. Make animations for them displaying this behavior

5. Move on to work with systems of neurons exhibiting canard explosions

6. Compare original reduced HH/FH-N model parameters to system parameters

## Tests

### Compute basic 2D Reduced HH Solution to an RTM neuron

Here, we just make initial pushes to create the functions to make a plot in order to verify that basic functionality is there. We used the parameters from page 32 from Börgers' textbook [1].

Code for the process of making this plot can be found in [tests/HodgkinHuxley.ipynb](tests/HodgkinHuxley.ipynb)

![Simulated 2D Reduced HodgkinHuxley RTM Neuron](assets/TwoDim_HH_RTM_test.png)

## References

[1] Börgers, Christoph. An Introduction to Modeling Neuronal Dynamics Christoph Börgers. Springer International Publishing Springer, 2018.
