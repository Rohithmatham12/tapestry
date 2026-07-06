override define help_targets_message
For the Flower WAN weight-transfer spike:

make flower-wan-spike-all  # Make all the following targets.

make flower-wan-spike-tests
                           # Run the Flower WAN spike unit tests.
endef

# This contribution depends on Flower runtime packages that are resolved from
# its own pyproject.toml. The root lint/type-check environment cannot resolve
# those imports yet, so keep these checks opt-in for the provisional spike.
pylint-default type-check-default:
	@echo "${WARN} ${skip-contrib-target}${_END}"
	@true
