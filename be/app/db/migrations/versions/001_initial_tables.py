"""create initial tables for campuses, faculties, and majors

Revision ID: 001_initial_tables
Revises: 
Create Date: 2026-09-15 11:15:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "001_initial_tables"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Create campuses table
    op.create_table(
        "campuses",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("short_name", sa.String(length=50), nullable=True),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("type", sa.String(length=50), server_default="PTN", nullable=False),
        sa.Column("accreditation", sa.String(length=20), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=False),
        sa.Column("province", sa.String(length=100), nullable=False),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("website", sa.String(length=255), nullable=True),
        sa.Column("logo_url", sa.String(length=500), nullable=True),
        sa.Column("banner_url", sa.String(length=500), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("ranking_national", sa.Integer(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_campuses_city"), "campuses", ["city"], unique=False)
    op.create_index(op.f("ix_campuses_name"), "campuses", ["name"], unique=False)
    op.create_index(op.f("ix_campuses_province"), "campuses", ["province"], unique=False)
    op.create_index(op.f("ix_campuses_short_name"), "campuses", ["short_name"], unique=False)
    op.create_index(op.f("ix_campuses_slug"), "campuses", ["slug"], unique=True)

    # 2. Create faculties table
    op.create_table(
        "faculties",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("campus_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["campus_id"], ["campuses.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_faculties_campus_id"), "faculties", ["campus_id"], unique=False)
    op.create_index(op.f("ix_faculties_slug"), "faculties", ["slug"], unique=False)

    # 3. Create majors table
    op.create_table(
        "majors",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("campus_id", sa.Integer(), nullable=False),
        sa.Column("faculty_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("degree", sa.String(length=20), server_default="S1", nullable=False),
        sa.Column("accreditation", sa.String(length=20), nullable=True),
        sa.Column("capacity", sa.Integer(), nullable=True),
        sa.Column("tuition_min", sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column("tuition_max", sa.Numeric(precision=12, scale=2), nullable=True),
        sa.Column("career_prospects", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["campus_id"], ["campuses.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["faculty_id"], ["faculties.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_majors_campus_id"), "majors", ["campus_id"], unique=False)
    op.create_index(op.f("ix_majors_faculty_id"), "majors", ["faculty_id"], unique=False)
    op.create_index(op.f("ix_majors_name"), "majors", ["name"], unique=False)
    op.create_index(op.f("ix_majors_slug"), "majors", ["slug"], unique=False)


def downgrade() -> None:
    op.drop_table("majors")
    op.drop_table("faculties")
    op.drop_table("campuses")
