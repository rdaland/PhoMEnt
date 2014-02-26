import sys
# Should this import should be inside the if statement below? -Michael

import megatableau, data_prob
import scipy, scipy.optimize
import parabolas

def learn_weights(mt):
    """ Given a filled-in megatableau, optimize and return its weight vector.
    """
    # Set up the initial weights and weight bounds (nonpositive reals)
    w_0 = -scipy.rand(len(mt.weights))
    nonpos_reals = [(-25,0) for wt in mt.weights]

    # Learn
    print(data_prob.nlpwg(w_0, mt.tableau))
    learned_weights, fneval, rc = scipy.optimize.fmin_tnc(data_prob.nlpwg, w_0, args = (mt.tableau,), bounds=nonpos_reals)

    ## Previous version below: tells fmin_tnc to approximate the gradient itself
    # learned_weights, fneval, rc = scipy.optimize.fmin_tnc(data_prob.neg_log_probability, w_0, args = (mt.tableau,), bounds=nonpos_reals, approx_grad=True)

    return learned_weights

def learn_parabola(c2,c1,c0):
    parab = parabolas.get_parabola(c2,c1,c0)
    x_0 = [0]
    learned_x, fneval, rc = scipy.optimize.fmin_tnc(parab, x_0)
    print "correct minimum: x =", parabolas.correct_parab_min(c2,c1,c0)
    print "learned minimum: x =", learned_x
    return learned_x

def learn_hyper_parabola(c2_c1_tuples, c0):
    hyperparab = parabolas.get_hyper_parabola(c2_c1_tuples,c0)
    xs_0 = [0 for x in c2_c1_tuples]
    learned_xs, fneval, rc = scipy.optimize.fmin_tnc(hyperparab, xs_0)
    print "correct minimum: xs =", parabolas.correct_hyper_parab_min(c2_c1_tuples,c0)
    print "learned minimum: xs =", learned_xs
    return learned_xs


if __name__ == '__main__':
    """ Runs if calc_weights.py is called from the shell rather than imported.
    """
    # Argument parsing
    assert len(sys.argv)==2
    tableau_file_name = sys.argv[1]

    # Read in data
    mt = megatableau.MegaTableau(tableau_file_name)

    # Learn and print
    mt.weights = learn_weights(mt)
    print('\nLearned weights:')
    for constraint,weight in zip(mt.constraints, mt.weights):
        print(constraint+'\t'+str(weight))