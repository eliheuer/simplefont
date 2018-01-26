from defcon import Glyph, Component, registerRepresentationFactory
from simplefont.representationFactories.glyphCellFactory import (
    TFGlyphCellFactory)
from simplefont.representationFactories.glyphViewFactory import (
    ComponentQPainterPathFactory, FilterSelectionFactory,
    SelectedContoursQPainterPathFactory, SelectedComponentsQPainterPathFactory,
    SplitLinesQPainterPathFactory)

# TODO: fine-tune the destructive notifications
_glyphFactories = {
    "SimpleFont.SelectedComponentsQPainterPath": (
        SelectedComponentsQPainterPathFactory,
        ("Glyph.Changed", "Glyph.SelectionChanged")),
    "SimpleFont.SplitLinesQPainterPath": (
        SplitLinesQPainterPathFactory, None),
    "SimpleFont.FilterSelection": (
        FilterSelectionFactory, ("Glyph.Changed", "Glyph.SelectionChanged")),
    "SimpleFont.SelectedContoursQPainterPath": (
        SelectedContoursQPainterPathFactory,
        ("Glyph.Changed", "Glyph.SelectionChanged")),
    "SimpleFont.GlyphCell": (
        TFGlyphCellFactory, None),
}
_componentFactories = {
    "SimpleFont.QPainterPath": (
        ComponentQPainterPathFactory, (
            "Component.Changed", "Component.BaseGlyphDataChanged")),
}


def registerAllFactories():
    for name, (factory, destructiveNotifications) in _glyphFactories.items():
        registerRepresentationFactory(
            Glyph, name, factory,
            destructiveNotifications=destructiveNotifications)
    for name, (factory, destructiveNotifications) in \
            _componentFactories.items():
        registerRepresentationFactory(
            Component, name, factory,
            destructiveNotifications=destructiveNotifications)
