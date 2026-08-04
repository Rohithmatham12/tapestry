"""Tests for data-management capability checks."""

from __future__ import annotations

import unittest

from tapestry.data import (
    DataParticipationMode,
    DataPipelineCapability,
    DataToolAssessment,
    allowed_modes_for_shared_training,
    ods_assessment_questions,
)


class DataManagementTest(unittest.TestCase):
    """Data capability and ODS assessment helpers."""

    def test_complete_data_tool_assessment_has_no_findings(self) -> None:
        assessment = DataToolAssessment(
            tool_name="candidate-catalog",
            supported_capabilities=frozenset(
                {
                    DataPipelineCapability.CATALOG,
                    DataPipelineCapability.POINTER_BASED_DATASETS,
                    DataPipelineCapability.STRUCTURED_RIGHTS_METADATA,
                    DataPipelineCapability.ACCESS_CONTROL,
                    DataPipelineCapability.EVENT_CAPTURE,
                    DataPipelineCapability.VISIBILITY_TIERS,
                    DataPipelineCapability.PORTABLE_SCHEMAS,
                }
            ),
        )

        self.assertEqual(assessment.missing_m1_capabilities, ())
        self.assertEqual(assessment.findings(), ())

    def test_assessment_reports_missing_capabilities_for_ods_research(self) -> None:
        assessment = DataToolAssessment(
            tool_name="Open Data Spaces",
            supported_capabilities=frozenset(
                {
                    DataPipelineCapability.CATALOG,
                    DataPipelineCapability.PORTABLE_SCHEMAS,
                }
            ),
        )

        missing = assessment.missing_m1_capabilities

        self.assertIn(DataPipelineCapability.ACCESS_CONTROL, missing)
        self.assertIn(DataPipelineCapability.EVENT_CAPTURE, missing)
        self.assertGreaterEqual(len(assessment.findings()), 5)

    def test_ods_questions_cover_viability_and_large_artifact_streaming(self) -> None:
        questions = " ".join(ods_assessment_questions())

        self.assertIn("active enough", questions)
        self.assertIn("stream large training artifacts", questions)
        self.assertIn("participant-local datasets", questions)

    def test_participant_private_mode_is_not_allowed_for_shared_training(self) -> None:
        modes = allowed_modes_for_shared_training()

        self.assertIn(DataParticipationMode.LOCAL_ONLY, modes)
        self.assertNotIn(DataParticipationMode.PARTICIPANT_PRIVATE, modes)


if __name__ == "__main__":
    unittest.main()
