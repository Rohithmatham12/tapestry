"""Tests for data-management capability checks."""

from __future__ import annotations

import unittest

from tapestry.data import (
    REQUIRED_DATA_CAPABILITIES,
    DataParticipationMode,
    DataPipelineCapability,
    DataToolAssessment,
    allowed_modes_for_shared_training,
)


class DataManagementTest(unittest.TestCase):
    """Data capability and ODS assessment helpers."""

    def test_complete_data_tool_assessment_has_no_findings(self) -> None:
        """A tool supporting all required capabilities has no findings."""
        assessment = DataToolAssessment(
            tool_name="candidate-catalog",
            supported_capabilities=REQUIRED_DATA_CAPABILITIES,
        )

        self.assertEqual(assessment.missing_capabilities, ())
        self.assertEqual(assessment.findings(), ())

    def test_participant_private_mode_is_not_allowed_for_shared_training(self) -> None:
        """Private-only data is excluded from shared-training participation."""
        modes = allowed_modes_for_shared_training()

        self.assertIn(DataParticipationMode.LOCAL_ONLY, modes)
        self.assertNotIn(DataParticipationMode.PARTICIPANT_PRIVATE, modes)


if __name__ == "__main__":
    unittest.main()
