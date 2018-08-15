@given(u'a role name')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a role name')


@when(u'executing ansible-runner with role option')
def step_impl(context):
    raise NotImplementedError(u'STEP: When executing ansible-runner with role option')


@then(u'run the role directly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then run the role directly')
